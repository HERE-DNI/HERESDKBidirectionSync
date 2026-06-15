---
title: "modes property"
slug: "sdk-for-flutter-explore-routing-transitrouteoptions-modes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- modes.html -->


<div>
<h1>modes property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-explore-routing-transitmode">TransitMode</a>&gt;
modes
<div class="features">getter/setter pair</div>


<p>This list is used to determine which transit modes should be used for route calculation,
<a href="sdk-for-flutter-explore-routing-transitrouteoptions-modefilter">TransitRouteOptions.modeFilter</a> specifies whether this list is an inclusion or an exclusion.
For example, specifying subway and bus transit modes with the include filter, returns only subway
and bus transit modes, and with the exclude filter, returns all the transit modes except subway
and bus. When not set, all the supported transit modes are permitted.
By default, this list is empty.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;TransitMode&gt; modes;</code></pre>

 



</div>
`
}</HTMLBlock>
