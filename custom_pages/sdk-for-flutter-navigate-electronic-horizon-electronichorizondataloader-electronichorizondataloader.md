---
title: "ElectronicHorizonDataLoader constructor"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-electronichorizondataloader"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonDataLoader.html -->


<div>
<h1>ElectronicHorizonDataLoader constructor</h1></div>

ElectronicHorizonDataLoader(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> sdkEngine, </li>
<li><a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a> options, </li>
<li>int segmentDataCacheSize</li>
</ol>)
    

<p>Creates a new instance of <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a>.</p>
<p>The constructor accepts options to configure the data loader. For more information, see <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a>.
The cache size limits the number of segments that the loader can keep in memory at the same time.</p>
<ul>
<li>
<p><code>sdkEngine</code> The <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> instance that provides shared services, such as networking and map data.</p>
</li>
<li>
<p><code>options</code> The <a href="sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class">SegmentDataLoaderOptions</a> instance that configures how segment data is requested.</p>
</li>
<li>
<p><code>segmentDataCacheSize</code> The maximum number of segments that the loader can cache.</p>
</li>
</ul>
<p>Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a> If the data loader cannot be created.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory ElectronicHorizonDataLoader(SDKNativeEngine sdkEngine, SegmentDataLoaderOptions options, int segmentDataCacheSize) =&gt; $prototype.make(sdkEngine, options, segmentDataCacheSize);</code></pre>

 



</div>
`
}</HTMLBlock>
