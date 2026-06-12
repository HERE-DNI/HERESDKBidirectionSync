---
title: "WarnerEngine class abstract"
slug: "sdk-for-flutter-navigate-warner-warnerengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarnerEngine-class.html -->


<div>
<h1>WarnerEngine class abstract</h1></div>

<p>Provides the core functionality for generating and managing navigation warnings.</p>
<p><code>WarnerEngine</code> processes Electronic Horizon data and determines when various types
of warnings should be issued. It is used with <a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class">ElectronicHorizonListener</a>,
which supply the road topology and positional updates required for warning evaluation.</p>
<p>The engine monitors enabled warning types and notifies registered listeners when new warnings become available.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-warnerengine-withenabledwarnings">WarnerEngine.WithEnabledWarnings</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-warnerengine-withengine">WarnerEngine.WithEngine</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-runtimetype">runtimeType</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-timingprofile">timingProfile</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-warningoptions">warningOptions</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-addcustomwarningprovider">addCustomWarningProvider</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-addenabledwarnings">addEnabledWarnings</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-addwarninglistener">addWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-clearcustomwarningproviders">clearCustomWarningProviders</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-finalizegivenwarnings">finalizeGivenWarnings</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-getcustomwarningnotificationdistances">getCustomWarningNotificationDistances</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-getenabledwarnings">getEnabledWarnings</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-getwarningnotificationdistances">getWarningNotificationDistances</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-getwarningsregistry">getWarningsRegistry</a></li><li><a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-onelectronichorizonupdated">onElectronicHorizonUpdated</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-removecustomwarningprovider">removeCustomWarningProvider</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-removeenabledwarnings">removeEnabledWarnings</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-removewarninglistener">removeWarningListener</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-setcustomwarningnotificationdistances">setCustomWarningNotificationDistances</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-setenabledwarnings">setEnabledWarnings</a></li><li><a href="/sdk-for-flutter-navigate-warner-warnerengine-setwarningnotificationdistances">setWarningNotificationDistances</a></li><li><a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
