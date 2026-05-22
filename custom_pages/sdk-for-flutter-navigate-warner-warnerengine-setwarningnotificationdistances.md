---
title: "Untitled"
slug: "sdk-for-flutter-navigate-warner-warnerengine-setwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setWarningNotificationDistances.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warnerengine-class</li>
<li class="self-crumb">setWarningNotificationDistances abstract method</li>
</ol>
<div class="self-name">setWarningNotificationDistances</div>
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
<div class="main-content" data-above-sidebar="warner/WarnerEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setWarningNotificationDistances abstract method</h1></div>
<section class="multi-line-signature">
bool
setWarningNotificationDistances(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-warningtype warningType, </li>
<li>/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class warningNotificationDistances</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the warning notification distances for the specified warning type.</p>
<p><strong>Note</strong>: /sdk-for-flutter-navigate-navigation-warningtype is not a valid value for this method.
Use /sdk-for-flutter-navigate-warner-warnerengine-setcustomwarningnotificationdistances to configure distances for a specific
custom warning type.</p>
<ul>
<li>
<p><code>warningType</code> The warning type for which the warning notification distances will be set.
Must not be /sdk-for-flutter-navigate-navigation-warningtype.</p>
</li>
<li>
<p><code>warningNotificationDistances</code> The warning notification distances to be set for the specified warning type.</p>
</li>
</ul>
<p>Returns <code>bool</code>. True if the distances were successfully set; false if <code>WarnerEngine.setWarningNotificationDistances.warningType</code> is
/sdk-for-flutter-navigate-navigation-warningtype or the options could not be applied.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool setWarningNotificationDistances(WarningType warningType, WarningNotificationDistances warningNotificationDistances);</code></pre>
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
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
<li>/sdk-for-flutter-navigate-warner-warnerengine-class</li>
<li class="self-crumb">setWarningNotificationDistances abstract method</li>
</ol>
<h5>WarnerEngine class</h5>
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
