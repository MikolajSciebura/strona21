import re
import sys

def minify_css(css):
    # Remove comments
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    # Remove whitespace
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{:;,])\s*', r'\1', css)
    return css.strip()

def minify_js(js):
    # Very basic JS minification: remove comments and some whitespace
    # Caution: this is not a full-blown minifier like Terser

    # Remove block comments
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)

    # Remove line comments, but try to avoid URLs
    # This looks for // that is not preceded by : (as in http://)
    js = re.sub(r'(?<!:)\/\/.*?\n', '\n', js)

    # This is risky for JS without a proper parser, so let's be conservative
    # Just remove multiple spaces and empty lines
    js = re.sub(r'\n\s*\n', '\n', js)
    return js.strip()

def main():
    if len(sys.argv) < 4:
        print("Usage: python minify.py <type> <input> <output>")
        return

    mode = sys.argv[1]
    infile = sys.argv[2]
    outfile = sys.argv[3]

    with open(infile, 'r') as f:
        content = f.read()

    if mode == 'css':
        minified = minify_css(content)
    elif mode == 'js':
        minified = minify_js(content)
    else:
        minified = content

    with open(outfile, 'w') as f:
        f.write(minified)

if __name__ == '__main__':
    main()
