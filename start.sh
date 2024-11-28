exec python -u api.py &
exec python -u agent.py &
streamlit run app.py --server.address=0.0.0.0 --server.port=7860
