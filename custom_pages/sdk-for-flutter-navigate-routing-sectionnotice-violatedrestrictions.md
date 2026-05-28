---
title: "violatedRestrictions property"
slug: "sdk-for-flutter-navigate-routing-sectionnotice-violatedrestrictions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- violatedRestrictions.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-sectionnotice-class</li>
<li class="self-crumb">violatedRestrictions property</li>
</ol>
<div class="self-name">violatedRestrictions</div>
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
<div class="main-content" data-above-sidebar="routing/SectionNotice-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>violatedRestrictions property</h1></div>
<section class="multi-line-signature">
        
        List&lt;<wbr/>/sdk-for-flutter-navigate-routing-violatedrestriction-class&gt;
violatedRestrictions
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>The following property <code>violated_restrictions</code> contains the notice detail information.
Only three types of restrictions can have notice details: time dependent restriction, vehicle restriction and transport mode restriction.
There is no one-to-one match of the <code>SectionNotice.code</code> and these three restriction types. For example, if <code>SectionNotice.code</code> is
/sdk-for-flutter-navigate-routing-sectionnoticecode, then it can be either vehicle restriction or transport mode restriction. If <code>SectionNotice.code</code> is
/sdk-for-flutter-navigate-routing-sectionnoticecode, then it is time dependent restriction.
If the section notice is none of the above-mentioned three types, then this will be an empty list.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;ViolatedRestriction&gt; violatedRestrictions;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-sectionnotice-class</li>
<li class="self-crumb">violatedRestrictions property</li>
</ol>
<h5>SectionNotice class</h5>
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
