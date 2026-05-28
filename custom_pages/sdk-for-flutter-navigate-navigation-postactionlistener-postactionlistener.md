---
title: "PostActionListener constructor"
slug: "sdk-for-flutter-navigate-navigation-postactionlistener-postactionlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PostActionListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-postactionlistener-class</li>
<li class="self-crumb">PostActionListener factory constructor</li>
</ol>
<div class="self-name">PostActionListener</div>
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
<div class="main-content" data-above-sidebar="navigation/PostActionListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>PostActionListener constructor</h1></div>
<section class="multi-line-signature">
PostActionListener(<wbr/><ol class="parameter-list single-line"> <li>void onPostActionsLambda(<ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-postaction-class&gt;</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class should be implemented in order to
receive post action notifications.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PostActionListener(
  void Function(List&lt;PostAction&gt;) onPostActionsLambda,

) =&gt; PostActionListener$Lambdas(
  onPostActionsLambda,

);</code></pre>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-postactionlistener-class</li>
<li class="self-crumb">PostActionListener factory constructor</li>
</ol>
<h5>PostActionListener class</h5>
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
