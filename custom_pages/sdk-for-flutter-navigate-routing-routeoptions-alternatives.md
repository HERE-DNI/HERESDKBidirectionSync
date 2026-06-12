---
title: "alternatives property"
slug: "sdk-for-flutter-navigate-routing-routeoptions-alternatives"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- alternatives.html -->


<div>
<h1>alternatives property</h1></div>

        
        int
        alternatives
<div class="features">getter/setter pair</div>


<p>Maximum number of alternative routes that will be calculated, in addition
to the best one. The provided value must be in the range [0, 6].
Alternative routes can be unavailable, thus they are not guaranteed to be returned.
The order of routes is from the best to the worst, as evaluated by the route calculation
algorithm and according to the given input parameters.
Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
Must be 0 for isoline calculation.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int alternatives;</code></pre>

 



</div>
`
}</HTMLBlock>
