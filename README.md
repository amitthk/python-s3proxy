# python-s3proxy

A script which works as a simple http proxy to an s3 bucket. Useful for accessing non-public s3 buckets via HTTP. Supports automatic serving of index.html when a URL ends in / and automatic building of simple indexes when index.html does not exist. Built for the specific use-case of hosting a private pypi repository in s3.

Usage:

<pre><code>
#export variables according to your preference
export S3_BUCKET=testbucket
export S3_PREFIX=''
export IAM_KEY=minioadmin
export IAM_SECRET=minioadmin
export BIND_HOST=0.0.0.0
export BIND_PORT=5000
export S3_ENDPOINT_URL=http://localhost:9000

#install the module
pip install -r requirements.pip
pip install .

#run
s3proxy
</code></pre>


