---
title: "getEnvironmentalZoneWarning abstract method"
slug: "sdk-for-flutter-navigate-warner-warningsregistry-getenvironmentalzonewarning"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getEnvironmentalZoneWarning.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warningsregistry-class</li>
<li class="self-crumb">getEnvironmentalZoneWarning abstract method</li>
</ol>
<div class="self-name">getEnvironmentalZoneWarning</div>
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
<h1>getEnvironmentalZoneWarning abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-navigation-environmentalzonewarning-class?
getEnvironmentalZoneWarning(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-warner-warning-class warning</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns environmental zone warning corresponding to the given identifier.</p>
<ul>
<li><code>warning</code> The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
The <code>warning</code> uniquely identifies a single environmental zone warning within this registry
and is used to retrieve its full metadata.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-navigation-environmentalzonewarning-class. The /sdk-for-flutter-navigate-navigation-environmentalzonewarning-class object associated with the provided <code>WarningsRegistry.getEnvironmentalZoneWarning.warning</code>,
or <code>null</code> if no warning exists for the given <code>WarningsRegistry.getEnvironmentalZoneWarning.warning</code>.
This object contains the full details and attributes of the corresponding warning.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">EnvironmentalZoneWarning? getEnvironmentalZoneWarning(Warning warning);</code></pre>
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
<li class="self-crumb">getEnvironmentalZoneWarning abstract method</li>
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
</div></div>
</div>
`
}</HTMLBlock>
