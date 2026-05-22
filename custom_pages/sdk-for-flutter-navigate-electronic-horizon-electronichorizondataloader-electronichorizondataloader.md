---
title: "Untitled"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-electronichorizondataloader"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonDataLoader.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class</li>
<li class="self-crumb">ElectronicHorizonDataLoader factory constructor</li>
</ol>
<div class="self-name">ElectronicHorizonDataLoader</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonDataLoader-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonDataLoader constructor</h1></div>
<section class="multi-line-signature">
ElectronicHorizonDataLoader(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, </li>
<li>/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class options, </li>
<li>int segmentDataCacheSize</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance of /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class.</p>
<p>The constructor accepts options to configure the data loader. For more information, see /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class.
The cache size limits the number of segments that the loader can keep in memory at the same time.</p>
<ul>
<li>
<p><code>sdkEngine</code> The /sdk-for-flutter-navigate-core-engine-sdknativeengine-class instance that provides shared services, such as networking and map data.</p>
</li>
<li>
<p><code>options</code> The /sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-class instance that configures how segment data is requested.</p>
</li>
<li>
<p><code>segmentDataCacheSize</code> The maximum number of segments that the loader can cache.</p>
</li>
</ul>
<p>Throws /sdk-for-flutter-navigate-core-errors-instantiationexception-class. /sdk-for-flutter-navigate-core-errors-instantiationexception-class If the data loader cannot be created.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory ElectronicHorizonDataLoader(SDKNativeEngine sdkEngine, SegmentDataLoaderOptions options, int segmentDataCacheSize) =&gt; $prototype.make(sdkEngine, options, segmentDataCacheSize);</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class</li>
<li class="self-crumb">ElectronicHorizonDataLoader factory constructor</li>
</ol>
<h5>ElectronicHorizonDataLoader class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
