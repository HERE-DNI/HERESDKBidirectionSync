---
title: "VisualNavigator.withNavigator constructor"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-visualnavigator-withnavigator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VisualNavigator.withNavigator.html -->


<div>
<h1>VisualNavigator.withNavigator constructor</h1></div>

VisualNavigator.withNavigator(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> navigator</li>
</ol>)
    

<p>Creates a new instance of this class using provided instance of <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> as source of data.</p>
<p><strong>Note:</strong> The <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a> implements the <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> interface and forwards
all calls to the underlying <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> instance. When multiple <a href="sdk-for-flutter-navigate-navigation-visualnavigator-class">VisualNavigator</a>
instances share the same <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> instance, method calls on this common instance
will overwrite changes made by another, which may lead to unexpected behavior.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>navigator</code> A NavigatorInterface implementation instance.</li>
</ul>
<p>Throws <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a>. <a href="sdk-for-flutter-navigate-core-errors-instantiationexception-class">InstantiationException</a> when operation fails.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VisualNavigator.withNavigator(NavigatorInterface navigator) =&gt; $prototype.withNavigator(navigator);</code></pre>

 



</div>
`
}</HTMLBlock>
