---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-heremap-debugdescribechildren"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- debugDescribeChildren.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/HereMap-class.html">/sdk-for-flutter-explore-mapview-heremap-class</a></li>
<li class="self-crumb">debugDescribeChildren method</li>
</ol>
<div class="self-name">debugDescribeChildren</div>
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
<h1>debugDescribeChildren method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@<a href="https://pub.dev/documentation/meta/1.17.0/meta/protected-constant.html">protected</a></li>
</ol>
</div>
List&lt;<wbr/>DiagnosticsNode&gt;
debugDescribeChildren(<wbr/>)

      <div class="features">inherited</div>
</section>
<section class="desc markdown">
<p>Returns a list of <code>DiagnosticsNode</code> objects describing this node's
children.</p>
<p>Children that are offstage should be added with <code>style</code> set to
<code>DiagnosticsTreeStyle.offstage</code> to indicate that they are offstage.</p>
<p>The list must not contain any null entries. If there are explicit null
children to report, consider <code>DiagnosticsNode.message</code> or
<code>DiagnosticsProperty&lt;Object&gt;</code> as possible <code>DiagnosticsNode</code> objects to
provide.</p>
<p>Used by <code>toStringDeep</code>, <code>toDiagnosticsNode</code> and <code>toStringShallow</code>.</p>
<p>See also:</p>
<ul>
<li><code>RenderTable.debugDescribeChildren</code>, which provides high quality custom
descriptions for its child nodes.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@protected
List&lt;DiagnosticsNode&gt; debugDescribeChildren() =&gt; const &lt;DiagnosticsNode&gt;[];</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/HereMap-class.html">/sdk-for-flutter-explore-mapview-heremap-class</a></li>
<li class="self-crumb">debugDescribeChildren method</li>
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
</HTMLBlock>
