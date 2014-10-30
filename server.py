#!/usr/bin/env python
import os
import random
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['base_uri'] = "http://product.christopher.su"

# ###################################################################
# Routes
# ###################################################################
products = ['alarm-clock', 'television', 'microwave', 'keyboard', 'water-bottle', 'eBook-reader', 'phone', 'chair', 'trash-can', 'stopwatch', 'wallet', 'keychain', 'bicycle', 'binder', 'notebook']
constraints = ['for-the-visually-impaired', 'for-the-elderly', 'for-children', 'for-families-with-children', 'for-the-hearing-impaired', 'for-the-speech-impaired', 'for-astronauts']
vowels = ['a', 'e', 'i', 'o', 'u']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', header='Product Prompt', title='Product Prompt', jumbotron='''
        <p class="lead" id="prompt">Click the button below to get a product design prompt!</p>
        <p><a class="btn btn-lg btn-success" id="prompt-btn" href="/random" role="button">Acquire Prompt</a></p>
        ''')

@app.route('/random', methods=['GET'])
def random():
    return render_template('redirect.html', url=app.config['base_uri'] + '/' + random.choice(products) + '/' + random.choice(constraints))

@app.route('/<product>/<constraint>', methods=['GET'])
def product_route(product, constraint):
    if product in products and constraint in constraints:
        product = product.replace('-', ' ')
        constraint = constraint.replace('-', ' ')

        prefix = "Design a "
        if product[0].lower() in vowels:
            prefix = "Design an "

        return render_template('index.html', header='Product Prompt', title = prefix + product + constrain, jumbotron='''
            <p class="lead" id="prompt">''' + prefix + product + constrain + '''</p>
            <p><a class="btn btn-success" id="prompt-btn" href="/random" role="button">Get Another Prompt</a></p>
            ''', body='''
    <div id="disqus_thread"></div>
    <script type="text/javascript">
        var disqus_shortname = 'productprompt';
        (function() {
            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
            dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
        })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
            ''')
    else:
        return render_template('redirect.html', url=app.config['base_uri'])

# ###################################################################
# Start Flask
# ###################################################################

if __name__ == '__main__':
    app.run(debug=True)