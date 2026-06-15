---
title: "getSegment abstract method"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-getsegment"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getSegment.html -->


<div>
<h1>getSegment abstract method</h1></div>

<a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderresult-class">ElectronicHorizonDataLoaderResult</a>
getSegment(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class">DirectedOCMSegmentId</a> segmentId</li>
</ol>)

      

    

<p>Returns loaded data for the given segment identifier.</p>
<p>The result contains either the loaded data or an error code.</p>
<ul>
<li><code>segmentId</code> The segment identifier for which to return the loaded data from the cache.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderresult-class">ElectronicHorizonDataLoaderResult</a>. The result object that contains either the loaded segment data or an error code.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ElectronicHorizonDataLoaderResult getSegment(DirectedOCMSegmentId segmentId);</code></pre>

 



</div>
`
}</HTMLBlock>
