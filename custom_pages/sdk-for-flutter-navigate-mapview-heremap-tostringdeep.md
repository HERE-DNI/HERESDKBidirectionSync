---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-heremap-tostringdeep"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toStringDeep.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-heremap-class</li>
<li class="self-crumb">toStringDeep method</li>
</ol>
<div class="self-name">toStringDeep</div>
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
<div class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>toStringDeep method</h1></div>
<section class="multi-line-signature">
String
toStringDeep(<wbr/>{<ol class="parameter-list"> <li>String prefixLineOne = '', </li>
<li>String? prefixOtherLines, </li>
<li>DiagnosticLevel minLevel = DiagnosticLevel.debug, </li>
<li>int wrapWidth = 65, </li>
</ol>})

      <div class="features">inherited</div>
</section>
<section class="desc markdown">
<p>Returns a string representation of this node and its descendants.</p>
<p><code>prefixLineOne</code> will be added to the front of the first line of the
output. <code>prefixOtherLines</code> will be added to the front of each other line.
If <code>prefixOtherLines</code> is null, the <code>prefixLineOne</code> is used for every line.
By default, there is no prefix.</p>
<p><code>minLevel</code> specifies the minimum <code>DiagnosticLevel</code> for properties included
in the output.</p>
<p><code>wrapWidth</code> specifies the column number where word wrapping will be
applied.</p>
<p>The <code>toStringDeep</code> method takes other arguments, but those are intended
for internal use when recursing to the descendants, and so can be ignored.</p>
<p>See also:</p>
<ul>
<li><code>toString</code>, for a brief description of the object but not its children.</li>
<li><code>toStringShallow</code>, for a detailed description of the object but not its
children.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String toStringDeep({
  String prefixLineOne = '',
  String? prefixOtherLines,
  DiagnosticLevel minLevel = DiagnosticLevel.debug,
  int wrapWidth = 65,
}) {
  return toDiagnosticsNode().toStringDeep(
    prefixLineOne: prefixLineOne,
    prefixOtherLines: prefixOtherLines,
    minLevel: minLevel,
    wrapWidth: wrapWidth,
  );
}</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-heremap-class</li>
<li class="self-crumb">toStringDeep method</li>
</ol>
<h5>HereMap class</h5>
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
