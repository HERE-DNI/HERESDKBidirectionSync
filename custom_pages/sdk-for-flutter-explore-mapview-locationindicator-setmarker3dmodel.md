---
title: "setMarker3dModel abstract method"
slug: "sdk-for-flutter-explore-mapview-locationindicator-setmarker3dmodel"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMarker3dModel.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-locationindicator-class</li>
<li class="self-crumb">setMarker3dModel abstract method</li>
</ol>
<div class="self-name">setMarker3dModel</div>
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
<div class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setMarker3dModel abstract method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.27.0. Please use the <code>setMarker3dModelWithRenderSizeUnit</code> instead.")</li>
</ol>
</div>
void
setMarker3dModel(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-mapmarker3dmodel-class model, </li>
<li>double scale, </li>
<li>/sdk-for-flutter-explore-mapview-locationindicatormarkertype type</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type.</p>
<p>The 3D model should be oriented with y axis up and thus standing on the x/z plane where the
z axis is the depth. The direction in which the location indicator is pointing is the
positive z axis. Please note that only MapMarker3DModel created from *.obj files are
supported. Models created from Mesh will be ignored.</p>
<ul>
<li>
<p><code>model</code> The MapMarker3DModel object to be displayed for the specified type. Only models
created from obj files are supported. Those created from mesh will be ignored.</p>
</li>
<li>
<p><code>scale</code> The scaling which will be applied to the marker model. As the size of the
location marker should be aligned on devices with different resolutions the
scale factor is applied relative to the ppi value and thus differs from the
scale which is passed to /sdk-for-flutter-explore-mapview-mapmarker3d-class objects.
Meter is used for the unit of the map marker 3d model coordinate system.
For historical reason, the scale factor is internally devided by 6.
To display a unit qube of 1x1x1 meter as is, please use a scale value of 6.0.</p>
</li>
<li>
<p><code>type</code> The type of location marker for which the marker 3d model should be replaced.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.27.0. Please use the `setMarker3dModelWithRenderSizeUnit` instead.")

void setMarker3dModel(MapMarker3DModel model, double scale, LocationIndicatorMarkerType type);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-locationindicator-class</li>
<li class="self-crumb">setMarker3dModel abstract method</li>
</ol>
<h5>LocationIndicator class</h5>
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
