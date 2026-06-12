---
title: "SegmentDataLoader class abstract"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentDataLoader-class.html -->


<div>
<h1>SegmentDataLoader class abstract</h1></div>

<p>Provides the abstract class for the access to the
segments data available in the local OCM map.</p>
<p>Please be aware that the methods within this class
load map data synchronously. In the event of absent data in the disk cache, the data will be
retrieved from the remote server. To mitigate the potential freezing of the calling thread,
it is advisable to proactively prefetch map data around the working area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-segmentdataloader">SegmentDataLoader</a></li><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-segmentdataloader-withengine">SegmentDataLoader.withEngine</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-downloadfile">downloadFile</a></li><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-getsegmentsaroundcoordinates">getSegmentsAroundCoordinates</a></li><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddata">loadData</a></li><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-loaddirectedsegmentdata">loadDirectedSegmentData</a></li><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
