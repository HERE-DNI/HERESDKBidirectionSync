---
title: "registerFont abstract method"
slug: "sdk-for-flutter-navigate-mapview-assetsmanager-registerfont"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- registerFont.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-assetsmanager-class</li>
<li class="self-crumb">registerFont abstract method</li>
</ol>
<div class="self-name">registerFont</div>
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
<div class="main-content" data-above-sidebar="mapview/AssetsManager-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>registerFont abstract method</h1></div>
<section class="multi-line-signature">
void
registerFont(<wbr/><ol class="parameter-list single-line"> <li>String fontName, </li>
<li>String fontPath</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Registers a font under a font name.</p>
<p>After registration, the font name can be used in</p>
<ul>
<li>the SVG <code>text</code> tag as <code>font-family</code> attribute parameter when creating a /sdk-for-flutter-navigate-mapview-mapimage-class with <code>ImageFormat.SVG</code>.</li>
<li>/sdk-for-flutter-navigate-mapview-mapmarkertextstyle-class</li>
</ul>
<p>Repeated registration with the same font name is ignored.</p>
<ul>
<li>
<p><code>fontName</code> A font name.</p>
</li>
<li>
<p><code>fontPath</code> A font file path. TTF, OTF and WOFF formats are supported.</p>
</li>
</ul>
<p>Can be an asset file path or an absolute file path.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void registerFont(String fontName, String fontPath);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-assetsmanager-class</li>
<li class="self-crumb">registerFont abstract method</li>
</ol>
<h5>AssetsManager class</h5>
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
