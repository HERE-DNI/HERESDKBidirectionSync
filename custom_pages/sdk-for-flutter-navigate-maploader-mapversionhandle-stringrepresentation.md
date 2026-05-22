---
title: "Untitled"
slug: "sdk-for-flutter-navigate-maploader-mapversionhandle-stringrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- stringRepresentation.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapversionhandle-class</li>
<li class="self-crumb">stringRepresentation abstract method</li>
</ol>
<div class="self-name">stringRepresentation</div>
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
<div class="main-content" data-above-sidebar="maploader/MapVersionHandle-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>stringRepresentation abstract method</h1></div>
<section class="multi-line-signature">
String
stringRepresentation(<wbr/><ol class="parameter-list single-line"> <li>String separator</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Returns a string representation of the map version in the format
"[cache-version][separator][offline-maps-version], [japan-cache-version][separator][japan-offline-maps-version]",
which can be obtained via <code>sdk.maploader.MapUpdater</code>.</p>
<ul>
<li><code>separator</code> Separator being used between elements of the map version.
In case map version has single element to it, separator is not used.
<code>none</code> token is used, when it is not possible to determine the version of the map.</li>
</ul>
<p>Examples:</p>
<ul>
<li>separator=", " possible result is "8.10, 9.10"</li>
<li>separator="."  possible result is "8.10.9.10"</li>
<li>separator="; " possible result is "8.10; 9.10"</li>
<li>separator="; " possible result is "8.10"</li>
</ul>
<p>Returns <code>String</code>. A string representation of the map version in the format</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String stringRepresentation(String separator);</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapversionhandle-class</li>
<li class="self-crumb">stringRepresentation abstract method</li>
</ol>
<h5>MapVersionHandle class</h5>
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
