---
title: "excludeChains property"
slug: "sdk-for-flutter-explore-search-categoryquery-excludechains"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- excludeChains.html -->


<div>
<h1>excludeChains property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-explore-search-placechain-class">PlaceChain</a>&gt;
excludeChains
<div class="features">getter/setter pair</div>


<p>List of chains to be excluded.
A place can be assigned multiple chains. If any of them is in <code>CategoryQuery.excludeChains</code>,
that place will not be included in the response, regardless of whether any of its assigned
chains have been included in <code>CategoryQuery.includeChains</code>.
In short, an exclusion will always win over an inclusion.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;PlaceChain&gt; excludeChains;</code></pre>

 



</div>
`
}</HTMLBlock>
