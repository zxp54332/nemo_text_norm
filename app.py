from flask import Flask, jsonify, request
from nemo_text_processing.text_normalization.normalize import Normalizer
from flask_apiexceptions import (
    JSONExceptionHandler,
    ApiException,
    ApiError,
    api_exception_handler,
)

app = Flask(__name__)
ext = JSONExceptionHandler(app)
ext.register(code_or_exception=ApiException, handler=api_exception_handler)

print("Initialize Normalizer...")
normalizer = Normalizer(input_case="cased", lang="en")

text_error = ApiError(code="text", message="Unable to process the text entity.")
conversion_error = ApiError(
    code="conversion", message="Unable to conversion the entity."
)


def get_text_norm(text):
    norm_text = None
    try:
        norm_text = normalizer.normalize(text)
    except Exception as e:
        raise ApiException(status_code=422, error=conversion_error)

    return norm_text


@app.route("/", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]

    # Empty input check
    if not text:
        raise ApiException(status_code=422, error=text_error)

    norm_text = get_text_norm(text)

    return jsonify(
        {
            "error": False,
            "err_msg": None,
            "norm_text": norm_text,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5252, debug=False)
