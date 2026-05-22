---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapimage-mapimage-withfilepathandwidthandheight"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImage.withFilePathAndWidthAndHeight.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapimage-class</li>
<li class="self-crumb">MapImage.withFilePathAndWidthAndHeight factory constructor</li>
</ol>
<div class="self-name">MapImage.withFilePathAndWidthAndHeight</div>
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
<div class="main-content" data-above-sidebar="mapview/MapImage-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MapImage.withFilePathAndWidthAndHeight constructor</h1></div>
<section class="multi-line-signature">
MapImage.withFilePathAndWidthAndHeight(<wbr/><ol class="parameter-list single-line"> <li>String filePath, </li>
<li>int width, </li>
<li>int height</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new map image from the provided path to the SVG Tiny or PNG image.</p>
<p>Will throw an error if either the height or width equals zero or the path is empty.</p>
<p>Trying to load a file that is not compliant with SVG Tiny or PNG results
in an undefined behavior. In particular, loading SVG that exceeds Tiny SVG
specification may result in an image that exhibits unexpected artifacts.</p>
<p>The caller must ensure that the file remains accessible for the entire duration of its usage by the
SDK. If that cannot be ensured, then it is recommended to either copy the file to a location that
remains accessible for the entire duration of its usage by the SDK or load and pass the file content
to one of the <code>MapImage</code> constructors that creates instances out of image data
(/sdk-for-flutter-navigate-mapview-mapimage-mapimage-withpixeldataandimageformat, /sdk-for-flutter-navigate-mapview-mapimage-mapimage-withimagedataimageformatwidthandheight).}</p>
<p>Please note that on iOS, file paths that originate, for example from a file picker (like <code>FilePicker</code>)
can be deleted by the system while the application is still running.</p>
<ul>
<li>
<p><code>filePath</code> The path to image file.</p>
</li>
<li>
<p><code>width</code> The width of image in pixels.</p>
</li>
<li>
<p><code>height</code> The height of image in pixels.</p>
</li>
</ul>
<p>Throws /sdk-for-flutter-navigate-core-errors-instantiationexception-class. Indicates what went wrong when the instantiation was attempted.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapImage.withFilePathAndWidthAndHeight(String filePath, int width, int height) =&gt; $prototype.withFilePathAndWidthAndHeight(filePath, width, height);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapimage-class</li>
<li class="self-crumb">MapImage.withFilePathAndWidthAndHeight factory constructor</li>
</ol>
<h5>MapImage class</h5>
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
