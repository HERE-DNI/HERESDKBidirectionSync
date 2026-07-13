---
title: "EngineOptions class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-engineoptions-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/EngineOptions-class-sidebar.html">

<div>

# <span class="kind-class">EngineOptions</span> class

</div>

<div class="section desc markdown">

Specifies several options specific to different engines.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-engine-engineoptions-engineoptions">EngineOptions</a></span><span class="signature">()</span>  
Creates a new instance with default values.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-engineoptions-customauthenticationmode">customAuthenticationMode</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-core-engine-authenticationmode-class">AuthenticationMode</a>?</span>  
Allows bearer authentication mode for engines. This mode adds a header ("Authorization", "Bearer \$Token") to each online request made by the module the object is added to. The token can either be provided directly or retrieved via key/secret from a dedicated backend.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-engineoptions-custombaseurl">customBaseUrl</a></span> <span class="signature">↔ String?</span>  
Allows engines to use custom base URLs for alternative services. By default, the available endpoints use HERE backend endpoints. If unsupported base URLs are specified, the related features will become non-functional. Please contact your HERE representative to learn about possible custom base URL usage options

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-engineoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-engineoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-engineoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-engineoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-engineoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

