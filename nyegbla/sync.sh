#!/usr/bin/bash

rsync -avz -e 'ssh -i ~/.ssh/prams.pem' nyegbla ubuntu@13.60.67.58:.
