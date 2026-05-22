---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapscenelights-setintensity"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setIntensity.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapscenelights-class</li>
<li class="self-crumb">setIntensity abstract method</li>
</ol>
<div class="self-name">setIntensity</div>
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
<div class="main-content" data-above-sidebar="mapview/MapSceneLights-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setIntensity abstract method</h1></div>
<section class="multi-line-signature">
void
setIntensity(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapscenelightscategory category, </li>
<li>double intensity, </li>
<li>/sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingcallback? callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Set a new intensity for the light based on its category.</p>
<ul>
<li>
<p><code>category</code> The category of light for which the intensity is set.</p>
</li>
<li>
<p><code>intensity</code> The light intensity value must be inside the range [0, 10].
The intensity value is clamped to this range.
If the value falls outside its supported range, it will be adjusted to stay within the range.
Note: When the intensity value is big,
3D objects might turn completely white because all the color channels could go over the limit of 1.0.</p>
</li>
<li>
<p><code>callback</code> Optional callback that will receive the result of this operation.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setIntensity(MapSceneLightsCategory category, double intensity, MapSceneLightsAttributeSettingCallback? callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapscenelights-class</li>
<li class="self-crumb">setIntensity abstract method</li>
</ol>
<h5>MapSceneLights class</h5>
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
