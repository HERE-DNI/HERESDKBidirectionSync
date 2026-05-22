---
title: "Untitled"
slug: "sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeexception"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- confirmHEREPrivacyNoticeException.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">confirmHEREPrivacyNoticeException abstract method</li>
</ol>
<div class="self-name">confirmHEREPrivacyNoticeException</div>
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
<div class="main-content" data-above-sidebar="location/LocationEngineBase-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>confirmHEREPrivacyNoticeException abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-location-confirmationstatus
confirmHEREPrivacyNoticeException(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>By calling this method, the application developer confirms that they have received an exceptional permission
from HERE in written form to <strong>not</strong> include a reference to the HERE Privacy Notice.</p>
<p>As a result,
the <code>LocationEngine</code> will not collect characteristic information about the nearby mobile and Wi-Fi network signals.
However, the engine will still be fully functional and it will deliver location updates when the exception
can be confirmed.
Note that this call should not involve user interaction and it should be executed silently
by the application before starting the <code>LocationEngine</code>.</p>
<p>The permission for exceptional use will be verified asynchronously using your HERE SDK credentials.
A missing permission will lead to stopping of the <code>LocationEngine</code> and /sdk-for-flutter-navigate-location-locationenginestatus
is delivered to <code>LocationStatusListener</code>.</p>
<p>It is not necessary to call this method on iOS platform.</p>
<p>Returns /sdk-for-flutter-navigate-location-confirmationstatus. Confirmation action status. Valid values are defined in /sdk-for-flutter-navigate-location-confirmationstatus.
A first-time call may result in /sdk-for-flutter-navigate-location-confirmationstatus, make sure to use the
<code>LocationStatusListener</code> to get notified on an unconfirmed permission.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ConfirmationStatus confirmHEREPrivacyNoticeException();</code></pre>
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
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-location-locationenginebase-class</li>
<li class="self-crumb">confirmHEREPrivacyNoticeException abstract method</li>
</ol>
<h5>LocationEngineBase class</h5>
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
