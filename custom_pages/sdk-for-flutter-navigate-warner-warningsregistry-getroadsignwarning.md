---
title: "Untitled"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getroadsignwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getRoadSignWarning.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warningsregistry-class</li>
<li class="self-crumb">getRoadSignWarning abstract method</li>
</ol>
<div class="self-name">getRoadSignWarning</div>
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
<div class="main-content" data-above-sidebar="warner/WarningsRegistry-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getRoadSignWarning abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-navigation-roadsignwarning-class?
getRoadSignWarning(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-warner-warning-class warning</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns a road-sign warning corresponding to the given identifier.</p>
<ul>
<li><code>warning</code> The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single road sign warning within this registry
and is used to retrieve its full metadata.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-navigation-roadsignwarning-class. The <code>sdk.navigation.RoadSignWarning</code> object associated with the provided <code>WarningsRegistry.getRoadSignWarning.warning</code>,
or <code>null</code> if no warning exists for the given <code>WarningsRegistry.getRoadSignWarning.warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RoadSignWarning? getRoadSignWarning(Warning warning);</code></pre>
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
<li>/sdk-for-flutter-navigate-warner-warningsregistry-class</li>
<li class="self-crumb">getRoadSignWarning abstract method</li>
</ol>
<h5>WarningsRegistry class</h5>
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
