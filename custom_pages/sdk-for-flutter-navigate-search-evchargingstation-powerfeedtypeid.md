---
title: "powerFeedTypeId property"
slug: "sdk-for-flutter-navigate-search-evchargingstation-powerfeedtypeid"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- powerFeedTypeId.html -->


<div>
<h1>powerFeedTypeId property</h1></div>

        
        String?
        powerFeedTypeId
<div class="features">getter/setter pair</div>


<p>ID of the power feed type, as defined by the
<a href="https://en.wikipedia.org/wiki/SAE_J1772#Charging">https://en.wikipedia.org/wiki/SAE_J1772#Charging</a> standard.
No data in case of offline search.
This field is always <code>null</code> for offline search using the <code>OfflineSearchEngine</code>. For online searches using the <code>SearchEngine</code>, it may be <code>null</code> if the data is unavailable.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String? powerFeedTypeId;</code></pre>

 



</div>
`
}</HTMLBlock>
