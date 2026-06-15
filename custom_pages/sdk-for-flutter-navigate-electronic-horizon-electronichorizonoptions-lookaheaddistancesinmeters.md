---
title: "lookAheadDistancesInMeters property"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-lookaheaddistancesinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAheadDistancesInMeters.html -->


<div>
<h1>lookAheadDistancesInMeters property</h1></div>

        
        List&lt;double&gt;
lookAheadDistancesInMeters
<div class="features">getter/setter pair</div>


<p>The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths.
The first entry of the list is for the most preferred path, the second is for the side paths of the first level,
the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided.
The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list.
If the list is empty, a single default distance value is used instead.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;double&gt; lookAheadDistancesInMeters;</code></pre>

 



</div>
`
}</HTMLBlock>
