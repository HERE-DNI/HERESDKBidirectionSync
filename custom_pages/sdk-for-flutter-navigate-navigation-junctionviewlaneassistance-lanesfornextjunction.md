---
title: "lanesForNextJunction property"
slug: "sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-lanesfornextjunction"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lanesForNextJunction.html -->


<div>
<h1>lanesForNextJunction property</h1></div>

        
        List&lt;<a href="/sdk-for-flutter-navigate-navigation-lane-class">Lane</a>&gt;
lanesForNextJunction
<div class="features">getter/setter pair</div>


<p>A list of lanes on the next complex junction.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
countries. An empty list means that the complex junction has been passed and that the lane information is not
valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
one event with an empty list afterwards.</p>
<p><strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;Lane&gt; lanesForNextJunction;</code></pre>

 



</div>
`
}</HTMLBlock>
