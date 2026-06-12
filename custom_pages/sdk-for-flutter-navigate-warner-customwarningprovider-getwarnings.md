---
title: "getWarnings abstract method"
slug: "sdk-for-flutter-navigate-warner-customwarningprovider-getwarnings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getWarnings.html -->


<div>
<h1>getWarnings abstract method</h1></div>

List&lt;<a href="/sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning</a>&gt;
getWarnings(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a> currentSegment, </li>
<li><a href="/sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>? previousSegment</li>
</ol>)

      

    

<p>Returns a list of custom warnings for the given vehicle position.</p>
<p>This method evaluates the custom warning provider using the current
vehicle position on the electronic horizon and returns the resulting
custom warnings along with corresponding payload.</p>
<ul>
<li>
<p><code>currentSegment</code> Segment data representing the vehicle’s current
position on the electronic horizon.</p>
</li>
<li>
<p><code>previousSegment</code> Segment data representing the vehicle’s previous
position on the electronic horizon. This parameter may be null if no
previous position information is available.</p>
</li>
</ul>
<p>Returns <code>List&lt;CustomWarning&gt;</code>. A list of <code>CustomWarning</code> instances representing all applicable
custom warnings. The list may be empty if no warnings apply.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;CustomWarning&gt; getWarnings(SegmentData currentSegment, SegmentData? previousSegment);</code></pre>

 



</div>
`
}</HTMLBlock>
