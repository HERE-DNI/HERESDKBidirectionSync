---
title: "eventTextListener property"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-eventtextlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- eventTextListener.html -->


<div>
<h1>eventTextListener property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>?
eventTextListener


<p>Object to receive text notifications when they are available.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
<strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.
Gets the listener that notifies when a text notification is available.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">EventTextListener? get eventTextListener;</code></pre>

</section>
<section id="setter">

void
eventTextListener=(<a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>? value)


<p>Object to receive text notifications when they are available.
Setting <code>null</code> value to the listener will unset the listener.
It returns <code>null</code> when no listener is set by an user.
<strong>Note:</strong> In order to receive the text notification emitted for the traffic merge warner,
when <code>TrafficMergeWarningOptions.enable_text_notification</code> has been enabled, the <code>sdk.navigation.EventTextListener</code> must be enabled as well.
Sets the listener that notifies when a text notification is available.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set eventTextListener(EventTextListener? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
