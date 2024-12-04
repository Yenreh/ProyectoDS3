#!/bin/bash
minikube delete
minikube start --driver=docker --nodes=3
