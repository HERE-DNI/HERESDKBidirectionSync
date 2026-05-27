---
title: "toDiagnosticsNode method"
slug: "sdk-for-flutter-explore-mapview-heremap-todiagnosticsnode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- toDiagnosticsNode.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-heremap-class</li>
<li class="self-crumb">toDiagnosticsNode method</li>
</ol>
<div class="self-name">toDiagnosticsNode</div>
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
<h1>toDiagnosticsNode method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@override</li>
</ol>
</div>
DiagnosticsNode
toDiagnosticsNode(<wbr/>{<ol class="parameter-list"> <li>String? name, </li>
<li>DiagnosticsTreeStyle? style, </li>
</ol>})

      <div class="features">inherited</div>
</section>
<section class="desc markdown">
<p>Returns a debug representation of the object that is used by debugging
tools and by <code>DiagnosticsNode.toStringDeep</code>.</p>
<p>Leave <code>name</code> as null if there is not a meaningful description of the
relationship between the this node and its parent.</p>
<p>Typically the <code>style</code> argument is only specified to indicate an atypical
relationship between the parent and the node. For example, pass
<code>DiagnosticsTreeStyle.offstage</code> to indicate that a node is offstage.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@override
DiagnosticsNode toDiagnosticsNode({String? name, DiagnosticsTreeStyle? style}) {
  return DiagnosticableTreeNode(name: name, value: this, style: style);
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-heremap-class</li>
<li class="self-crumb">toDiagnosticsNode method</li>
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
</div></div>
</div>
`
}</HTMLBlock>
