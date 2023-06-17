import streamlit as st
from streamlit.components.v1 import html

# Define the CSS styles as a string
css_styles = '''
<style>
body {
  background-color: #f5f5f5;
}

h1 {
  color: blue;
}
</style>
'''

# Define the HTML content
html_content = '''
<h1>This is a heading</h1>
<p>This is a paragraph with custom styles.</p>
'''

# Combine the CSS styles and HTML content
styled_html = css_styles + html_content

# Render the HTML content with the applied styles using st.components.v1.html
st.components.v1.html(styled_html, height=300)
