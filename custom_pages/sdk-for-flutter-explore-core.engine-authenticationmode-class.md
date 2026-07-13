---
title: "AuthenticationMode class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-authenticationmode-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AuthenticationMode-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/AuthenticationMode-class-sidebar.html">

<div>

# <span class="kind-class">AuthenticationMode</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This is a bearer authentication mode which adds or does not add a header ("Authorization", "Bearer \$Token") to each online request of the module the object is added to.

The token (if used) can be provided or is retrieved via key/secret from a dedicated backend.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-authenticationmode">AuthenticationMode</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-withexternal">withExternal</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-engine-authenticationmode-class">AuthenticationMode</a></span> </span>  
Assumes the authentication is provided by the client.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-withkeysecret">withKeySecret</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withKeySecret-param-accessKeyId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">accessKeyId</span>, </span><span id="sdk-for-flutter-explore-withKeySecret-param-accessKeySecret" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">accessKeySecret</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-engine-authenticationmode-class">AuthenticationMode</a></span> </span>  
SDK will authenticate with access key id access key secret to obtain authentication token.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-withtoken">withToken</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withToken-param-accessToken" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">accessToken</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-engine-authenticationmode-class">AuthenticationMode</a></span> </span>  
SDK will pass access token as a Bearer.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-authenticationmode-withtokenprovider">withTokenProvider</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withTokenProvider-param-tokenProvider" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-authenticationmodeaccesstokenprovider">AuthenticationModeAccessTokenProvider</a></span> <span class="parameter-name">tokenProvider</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-core-engine-authenticationmode-class">AuthenticationMode</a></span> </span>  
SDK will use access token provider to retrieve access token.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
