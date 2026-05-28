---
title: "ElectronicHorizonDataLoaderStatusListener constructor"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-electronichorizondataloaderstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonDataLoaderStatusListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-class</li>
<li class="self-crumb">ElectronicHorizonDataLoaderStatusListener factory constructor</li>
</ol>
<div class="self-name">ElectronicHorizonDataLoaderStatusListener</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonDataLoaderStatusListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonDataLoaderStatusListener constructor</h1></div>
<section class="multi-line-signature">
ElectronicHorizonDataLoaderStatusListener(<wbr/><ol class="parameter-list single-line"> <li>void onElectronicHorizonDataLoaderStatusUpdatedLambda(<ol class="parameter-list single-line"> <li>Map&lt;<wbr/>int, /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloadedstatus&gt;</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Provides a listener for status updates from the /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-loaddata method.</p>
<p>The listener receives the current state for different levels of the paths as /sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloadedstatus.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory ElectronicHorizonDataLoaderStatusListener(
  void Function(Map&lt;int, ElectronicHorizonDataLoadedStatus&gt;) onElectronicHorizonDataLoaderStatusUpdatedLambda,

) =&gt; ElectronicHorizonDataLoaderStatusListener$Lambdas(
  onElectronicHorizonDataLoaderStatusUpdatedLambda,

);</code></pre>
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
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-class</li>
<li class="self-crumb">ElectronicHorizonDataLoaderStatusListener factory constructor</li>
</ol>
<h5>ElectronicHorizonDataLoaderStatusListener class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
