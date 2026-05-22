---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapscenelightsattributesettingcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapSceneLightsAttributeSettingCallback.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapSceneLightsAttributeSettingCallback typedef</li>
</ol>
<div class="self-name">MapSceneLightsAttributeSettingCallback</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapSceneLightsAttributeSettingCallback typedef</h1></div>
<section class="multi-line-signature">
MapSceneLightsAttributeSettingCallback =
     void Function(/sdk-for-flutter-explore-mapview-mapscenelightsattributesettingerror? setLightError)
</section>
<section class="desc markdown">
<p>This callback function allows handling errors that occur during the setting of light attributes.</p>
<ul>
<li><code>setLightError</code> The cause for the failure when setting the light attributes, or <code>null</code> if no error occurred.</li>
</ul>
<p>Note: The error code <code>NO_LIGHTS</code> may be returned when attempting to set light attributes in map schemes
that do not support lights, for instance <code>road.network</code> map scheme.</p>
<p>Please refer to the error code documentation for further details on error handling.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef MapSceneLightsAttributeSettingCallback = void Function(MapSceneLightsAttributeSettingError? setLightError);</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapSceneLightsAttributeSettingCallback typedef</li>
</ol>
<h5>mapview library</h5>
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
