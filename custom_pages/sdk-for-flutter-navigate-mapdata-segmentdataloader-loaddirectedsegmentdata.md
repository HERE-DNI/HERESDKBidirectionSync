---
title: "loadDirectedSegmentData abstract method"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadDirectedSegmentData.html -->


<div>
<h1>loadDirectedSegmentData abstract method</h1></div>

<a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>
loadDirectedSegmentData(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapdata-directedocmsegmentid-class">DirectedOCMSegmentId</a> segment, </li>
<li><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a> options</li>
</ol>)

      

    

<p>Synchronously load the data for the given map directed segment.</p>
<ul>
<li>
<p><code>segment</code> The directed segment to load.</p>
</li>
<li>
<p><code>options</code> Request options</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>. Requested data of a segment.</p>
<p>Throws <a href="sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why list of data of a segment is not returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SegmentData loadDirectedSegmentData(DirectedOCMSegmentId segment, SegmentDataLoaderOptions options);</code></pre>

 



</div>
`
}</HTMLBlock>
