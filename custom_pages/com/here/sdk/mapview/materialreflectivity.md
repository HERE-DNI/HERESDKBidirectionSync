---
title: "MaterialReflectivity (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaterialreflectivity"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MaterialReflectivity

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MaterialReflectivity
------------------------------------------------------------------------
public final class MaterialReflectivity extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Material reflectivity properties are used to enable per‑pixel lighting for supported map objects (e.g. `LocationIndicator` markers and their halo).

## Lighting OFF vs ON

By default (when no MaterialReflectivity is assigned) objects are rendered "unlit" (emissive): their texture / color appears at a constant brightness, unaffected by scene lights. Assigning a `MaterialReflectivity` instance to an object that supports it (e.g. `LocationIndicator.materialReflectivity`) automatically enables lighting for this object and all its internal components. Clearing (setting the property to `null`) disables lighting again and restores the unlit appearance.

## Factors

Both factors are expected to be within \[0.0, 1.0\]. Values outside this range are allowed but may produce exaggerated results or be clamped by future implementations. Typical useful ranges:

- ambientFactor: 0.0 – 0.4 (higher values flatten the shading and reduce directional contrast)
- diffuseFactor: 0.5 – 1.0 (lower values dim the object under directional light)

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [ambientFactor](#ambientFactor)

The ambient factor controls how much of the object's base color is treated as constant ambient contribution (independent of light direction) when lighting is enabled.

`double`

  [diffuseFactor](#diffuseFactor)

The diffuse factor controls how much of the object's color contributes to the diffuse lighting component when lighting is enabled.

## Constructor Summary

Constructors

Constructor

  Description

  [MaterialReflectivity](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### ambientFactor

public double ambientFactor

    The ambient factor controls how much of the object's base color is treated as constant ambient contribution (independent of light direction) when lighting is enabled. Default value is 0.0.

### diffuseFactor

public double diffuseFactor

    The diffuse factor controls how much of the object's color contributes to the diffuse lighting component when lighting is enabled. Default value is 1.0.

## Constructor Details

  - ()" class="section detail">

### MaterialReflectivity

public MaterialReflectivity()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
