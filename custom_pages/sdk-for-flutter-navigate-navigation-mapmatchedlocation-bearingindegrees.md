---
title: "bearingInDegrees property"
slug: "sdk-for-flutter-navigate-navigation-mapmatchedlocation-bearingindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- bearingInDegrees.html -->


<div>
<h1>bearingInDegrees property</h1></div>

        
        double?
        bearingInDegrees
<div class="features">getter/setter pair</div>


<p>The bearing orientation points to the direction of travel, and has the same angle as the
street where it is matched to. Therefore, it must not necessarily be the same as the
bearing of a location source.
Starts at 0 in the geographic north and rotates in a clockwise direction around the
compass. It means that for going north it's equal to 0, for northeast it's equal to 45,
for east it's equal to 90, and so on.
If it cannot be determined, the value is <code>null</code>. Otherwise, it is guaranteed to be in the
range [0, 360).</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? bearingInDegrees;</code></pre>

 



</div>
`
}</HTMLBlock>
