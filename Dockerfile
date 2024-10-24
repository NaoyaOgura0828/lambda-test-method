FROM public.ecr.aws/lambda/python:3.12

COPY test_method.py "${LAMBDA_TASK_ROOT}"

CMD ["test_method.lambda_handler"]
