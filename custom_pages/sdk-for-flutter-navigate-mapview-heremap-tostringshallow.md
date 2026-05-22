---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-heremap-tostringshallow"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toStringShallow.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-heremap-class</li>
<li class="self-crumb">toStringShallow method</li>
</ol>
<div class="self-name">toStringShallow</div>
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
<h1>toStringShallow method</h1></div>
<section class="multi-line-signature">
String
toStringShallow(<wbr/>{<ol class="parameter-list"> <li>String joiner = ', ', </li>
<li>DiagnosticLevel minLevel = DiagnosticLevel.debug, </li>
</ol>})

      <div class="features">inherited</div>
</section>
<section class="desc markdown">
<p>Returns a one-line detailed description of the object.</p>
<p>This description is often somewhat long. This includes the same
information given by <code>toStringDeep</code>, but does not recurse to any children.</p>
<p><code>joiner</code> specifies the string which is place between each part obtained
from <code>debugFillProperties</code>. Passing a string such as <code>'\n '</code> will result
in a multiline string that indents the properties of the object below its
name (as per <code>toString</code>).</p>
<p><code>minLevel</code> specifies the minimum <code>DiagnosticLevel</code> for properties included
in the output.</p>
<p>See also:</p>
<ul>
<li><code>toString</code>, for a brief description of the object.</li>
<li><code>toStringDeep</code>, for a description of the subtree rooted at this object.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String toStringShallow({String joiner = ', ', DiagnosticLevel minLevel = DiagnosticLevel.debug}) {
  String? shallowString;
  assert(() {
    final StringBuffer result = StringBuffer();
    result.write(toString());
    result.write(joiner);
    final DiagnosticPropertiesBuilder builder = DiagnosticPropertiesBuilder();
    debugFillProperties(builder);
    result.write(
      builder.properties.where((DiagnosticsNode n) =&gt; !n.isFiltered(minLevel)).join(joiner),
    );
    shallowString = result.toString();
    return true;
  }());
  return shallowString ?? toString();
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
<li class="self-crumb">toStringShallow method</li>
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
