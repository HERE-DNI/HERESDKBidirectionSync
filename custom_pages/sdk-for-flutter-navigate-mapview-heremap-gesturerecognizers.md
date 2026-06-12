---
title: "gestureRecognizers property"
slug: "sdk-for-flutter-navigate-mapview-heremap-gesturerecognizers"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- gestureRecognizers.html -->


<div>
<h1>gestureRecognizers property</h1></div>

        
        Set&lt;Factory&lt;OneSequenceGestureRecognizer&gt;&gt;?
        gestureRecognizers
<div class="features">final</div>


<p>Which gestures should be consumed by the map.</p>
<p>It is possible for other gesture recognizers to be competing with the map on pointer
events, e.g if the map is inside a <code>ListView</code> the <code>ListView</code> will want to handle
vertical drags. The map will claim gestures that are recognized by any of the
recognizers on this list.</p>
<p>When this set is empty or null, the map will only handle pointer events for gestures that
were not claimed by any other gesture recognizer.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">final Set&lt;Factory&lt;OneSequenceGestureRecognizer&gt;&gt;? gestureRecognizers;</code></pre>

 



</div>
`
}</HTMLBlock>
