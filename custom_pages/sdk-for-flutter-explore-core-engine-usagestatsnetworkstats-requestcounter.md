---
title: "requestCounter property"
slug: "sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-requestcounter"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- requestCounter.html -->


<div>
<h1>requestCounter property</h1></div>

        
        int
        requestCounter
<div class="features">getter/setter pair</div>


<p>Amount of calls for particular family of methodCall.
methodCall in this case is considered as base request,
additional query params are ignored, all calculated as one request.
e.g. <a href="https://search.hereapi.com/someparams">https://search.hereapi.com/someparams</a> and <a href="https://search.hereapi.com/someparams2">https://search.hereapi.com/someparams2</a>
will be considered as 1 methodCall, and requestCounter is 2.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int requestCounter;</code></pre>

 



</div>
`
}</HTMLBlock>
