---
title: "MilestoneStatusListener constructor"
slug: "sdk-for-flutter-navigate-navigation-milestonestatuslistener-milestonestatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MilestoneStatusListener.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-milestonestatuslistener-class</li>
<li class="self-crumb">MilestoneStatusListener factory constructor</li>
</ol>
<div class="self-name">MilestoneStatusListener</div>
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
<div class="main-content" data-above-sidebar="navigation/MilestoneStatusListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>MilestoneStatusListener constructor</h1></div>
<section class="multi-line-signature">
MilestoneStatusListener(<wbr/><ol class="parameter-list single-line"> <li>void onMilestoneStatusUpdatedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-milestone-class, </li>
<li>/sdk-for-flutter-navigate-navigation-milestonestatus</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>This abstract class should be
implemented in order to receive notifications from this class about the
arrival at each /sdk-for-flutter-navigate-navigation-milestone-class or missing it.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MilestoneStatusListener(
  void Function(Milestone, MilestoneStatus) onMilestoneStatusUpdatedLambda,

) =&gt; MilestoneStatusListener$Lambdas(
  onMilestoneStatusUpdatedLambda,

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
<li>/sdk-for-flutter-navigate-navigation-milestonestatuslistener-class</li>
<li class="self-crumb">MilestoneStatusListener factory constructor</li>
</ol>
<h5>MilestoneStatusListener class</h5>
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
