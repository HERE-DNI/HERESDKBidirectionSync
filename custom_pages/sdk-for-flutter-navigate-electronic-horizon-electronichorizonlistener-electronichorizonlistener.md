---
title: "ElectronicHorizonListener constructor"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-electronichorizonlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class</li>
<li class="self-crumb">ElectronicHorizonListener factory constructor</li>
</ol>
<div class="self-name">ElectronicHorizonListener</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/ElectronicHorizonListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonListener constructor</h1></div>
<section class="multi-line-signature">
ElectronicHorizonListener(<wbr/><ol class="parameter-list single-line"> <li>void onElectronicHorizonUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonerrorcode?, </li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class?</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Provides a listener for receiving updates during execution of the /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-update method.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory ElectronicHorizonListener(
  void Function(ElectronicHorizonErrorCode?, ElectronicHorizonUpdate?) onElectronicHorizonUpdatedLambda,

) =&gt; ElectronicHorizonListener$Lambdas(
  onElectronicHorizonUpdatedLambda,

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
<li>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class</li>
<li class="self-crumb">ElectronicHorizonListener factory constructor</li>
</ol>
<h5>ElectronicHorizonListener class</h5>
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
