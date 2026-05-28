---
title: "CustomWarningProvider constructor"
slug: "sdk-for-flutter-navigate-warner-customwarningprovider-customwarningprovider"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomWarningProvider.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-customwarningprovider-class</li>
<li class="self-crumb">CustomWarningProvider factory constructor</li>
</ol>
<div class="self-name">CustomWarningProvider</div>
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
<div class="main-content" data-above-sidebar="warner/CustomWarningProvider-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>CustomWarningProvider constructor</h1></div>
<section class="multi-line-signature">
CustomWarningProvider(<wbr/><ol class="parameter-list single-line"> <li>int getCustomWarningTypeLambda(), </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-warner-customwarning-class&gt; getWarningsLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapdata-segmentdata-class, </li>
<li>/sdk-for-flutter-navigate-mapdata-segmentdata-class?</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>A abstract class representing a provider of custom warnings based on vehicle position.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory CustomWarningProvider(
  int Function() getCustomWarningTypeLambda,
  List&lt;CustomWarning&gt; Function(SegmentData, SegmentData?) getWarningsLambda,

) =&gt; CustomWarningProvider$Lambdas(
  getCustomWarningTypeLambda,
  getWarningsLambda,

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
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-customwarningprovider-class</li>
<li class="self-crumb">CustomWarningProvider factory constructor</li>
</ol>
<h5>CustomWarningProvider class</h5>
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
