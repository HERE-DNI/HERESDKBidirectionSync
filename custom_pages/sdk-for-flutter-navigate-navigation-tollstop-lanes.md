---
title: "lanes property"
slug: "sdk-for-flutter-navigate-navigation-tollstop-lanes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lanes.html -->


<div>
<h1>lanes property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-navigate-navigation-tollboothlane-class">TollBoothLane</a>&gt;
lanes
<div class="features">getter/setter pair</div>


<p>Describes the features of the booth for the lane.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
countries. An empty list means that the complex junction has been passed and that the lane information is not
valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
one event with an empty list afterwards.</p>
<p><strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;TollBoothLane&gt; lanes;</code></pre>

 



</div>
`
}</HTMLBlock>
