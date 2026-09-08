import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Level Devil", layout="wide")

game_html = """
<!DOCTYPE html>
<html>
<head>
<style>
  body { margin: 0; display: flex; justify-content: center; background: #f5eef8; }
  canvas { border: 2px solid #645573; border-radius: 8px; background: #f5eef8; }
</style>
</head>
<body>
<canvas id="gameCanvas" width="800" height="600" tabindex="1"></canvas>
<script>
  // Game logic, input listeners, and canvas draw calls run here
</script>
</body>
</html>
"""

components.html(game_html, height=620, width=820)