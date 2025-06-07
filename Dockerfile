FROM python:3.11-slim
WORKDIR /app
COPY ai_agent.py README.md ./
RUN pip install --no-cache-dir openai transformers
ENTRYPOINT ["python", "ai_agent.py"]
CMD []
